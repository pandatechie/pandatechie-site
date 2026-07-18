// Reveal on scroll — now has matching CSS (see site.css .reveal / .reveal.active)
(function(){
  var observerOptions = { threshold: 0.12 };
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('section, .bento-item, .reveal-item').forEach(function(el){
    el.classList.add('reveal');
    observer.observe(el);
  });

  // Sticky navbar subtle shrink — now applied consistently on every page,
  // not just the blog archive export
  var nav = document.querySelector('nav');
  if (nav) {
    window.addEventListener('scroll', function(){
      if (window.scrollY > 50) {
        nav.classList.add('h-16', 'shadow-sm');
        nav.classList.remove('h-20');
      } else {
        nav.classList.add('h-20');
        nav.classList.remove('h-16', 'shadow-sm');
      }
    });
  }

  // Smooth scroll for in-page anchors
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor){
    anchor.addEventListener('click', function(e){
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Card hover micro-interaction (mirrors the Stitch export, kept for parity)
  document.querySelectorAll('.card-hover').forEach(function(card){
    card.addEventListener('mouseenter', function(){ card.style.borderColor = 'rgba(82, 134, 225, 0.5)'; });
    card.addEventListener('mouseleave', function(){ card.style.borderColor = ''; });
  });
})();
