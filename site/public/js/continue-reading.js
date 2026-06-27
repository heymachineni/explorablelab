(function () {
  const STORAGE_KEY = 'explorablelab:recent';
  const MAX_ITEMS = 8;

  function readRecent() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch {
      return [];
    }
  }

  function writeRecent(items) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(items.slice(0, MAX_ITEMS)));
  }

  function trackPage(payload) {
    if (!payload?.slug || !payload?.href) return;
    const items = readRecent().filter((item) => item.slug !== payload.slug);
    items.unshift({
      slug: payload.slug,
      title: payload.title || payload.slug.replace(/-/g, ' '),
      href: payload.href,
      type: payload.type || '',
      typeCode: payload.typeCode || '',
      hub: payload.hub || '',
      viewedAt: Date.now(),
      pathSlug: payload.pathSlug || null,
      stepIndex: payload.stepIndex ?? null,
    });
    writeRecent(items);
    document.dispatchEvent(new CustomEvent('recent-updated'));
  }

  function formatWhen(ts) {
    const diff = Date.now() - ts;
    const mins = Math.floor(diff / 60000);
    if (mins < 1) return 'Just now';
    if (mins < 60) return `${mins}m ago`;
    const hours = Math.floor(mins / 60);
    if (hours < 24) return `${hours}h ago`;
    const days = Math.floor(hours / 24);
    return days === 1 ? 'Yesterday' : `${days}d ago`;
  }

  function renderContinueSection(container) {
    if (!container) return;
    const items = readRecent();
    if (!items.length) {
      container.hidden = true;
      return;
    }
    container.hidden = false;
    const list = container.querySelector('[data-continue-list]');
    if (!list) return;

    const icons = window.__continueIcons || {};
    const typeIcons = icons.typeIcons || {};
    const chevronSvg = icons.chevronSvg || '';
    const pageSvg = icons.pageSvg || '';

    list.innerHTML = items
      .slice(0, 5)
      .map((item) => {
        const icon = typeIcons[item.typeCode] || pageSvg;
        const meta = `${item.type || 'Reading'}${item.hub ? ` · ${item.hub}` : ''} · ${formatWhen(item.viewedAt)}`;
        return `
        <li class="page-row">
          <a href="${item.href}" class="page-row-link">
            <span class="page-row-icon">${icon}</span>
            <span class="page-row-body">
              <span class="page-row-title">${item.title}</span>
              <span class="page-row-summary">${meta}</span>
            </span>
            ${chevronSvg}
          </a>
        </li>`;
      })
      .join('');
  }

  function initContinueSections() {
    document.querySelectorAll('[data-continue-section]').forEach(renderContinueSection);
  }

  window.ExplorableLabContinue = {
    trackPage,
    readRecent,
    renderContinueSection,
  };

  document.addEventListener('DOMContentLoaded', initContinueSections);
  document.addEventListener('recent-updated', initContinueSections);
})();
