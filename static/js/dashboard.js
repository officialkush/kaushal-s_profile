// =========================================
// DASHBOARD ADMIN JS
// =========================================

document.addEventListener('DOMContentLoaded', () => {

  // ---------- Mobile nav toggle ----------
  const toggle = document.getElementById('dashNavToggle');
  const nav = document.getElementById('dashNav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      toggle.innerHTML = isOpen ? '<i class="fas fa-xmark"></i>' : '<i class="fas fa-bars"></i>';
    });

    // Close menu after a link is tapped (mobile)
    nav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.innerHTML = '<i class="fas fa-bars"></i>';
      });
    });
  }

  // ---------- Profile photo live preview ----------
  const photoInput = document.querySelector('input[type="file"][name="photo"]');
  const photoPreview = document.getElementById('photoPreview');
  if (photoInput && photoPreview) {
    photoInput.addEventListener('change', () => {
      const file = photoInput.files && photoInput.files[0];
      if (!file) return;
      const url = URL.createObjectURL(file);
      if (photoPreview.tagName === 'IMG') {
        photoPreview.src = url;
      } else {
        const img = document.createElement('img');
        img.src = url;
        img.alt = 'Photo preview';
        img.className = 'dash-photo-preview';
        img.id = 'photoPreview';
        photoPreview.replaceWith(img);
      }
    });
  }

});