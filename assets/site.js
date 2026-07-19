// Reveal on scroll — see site.css .reveal / .reveal.active
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

  // Sticky navbar subtle shrink
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

  // Card hover micro-interaction
  document.querySelectorAll('.card-hover').forEach(function(card){
    card.addEventListener('mouseenter', function(){ card.style.borderColor = 'rgba(255, 106, 61, 0.5)'; });
    card.addEventListener('mouseleave', function(){ card.style.borderColor = ''; });
  });

  // Count-up on stat numbers — was in the original mockup, dropped during the
  // Stitch port, restored here. Add data-count="N" (optionally data-suffix="+")
  // to any element to make it count up when it scrolls into view.
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length) {
    var counterIO = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if (entry.isIntersecting) {
          var el = entry.target;
          var target = parseInt(el.dataset.count, 10);
          var suffix = el.dataset.suffix || '';
          var duration = 1000;
          var start = performance.now();
          function tick(now){
            var progress = Math.min((now - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(eased * target) + suffix;
            if (progress < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
          counterIO.unobserve(el);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach(function(el){ counterIO.observe(el); });
  }

  // Magnetic pull on primary buttons — cursor nudges the button toward itself
  // within a small radius. Skipped entirely on touch devices.
  if (window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.magnetic').forEach(function(btn){
      btn.addEventListener('mousemove', function(e){
        var rect = btn.getBoundingClientRect();
        var x = e.clientX - rect.left - rect.width / 2;
        var y = e.clientY - rect.top - rect.height / 2;
        btn.style.transform = 'translate(' + (x * 0.25) + 'px, ' + (y * 0.35) + 'px)';
      });
      btn.addEventListener('mouseleave', function(){
        btn.style.transform = '';
      });
    });
  }

  // Panda easter egg — click the wordmark 5 times, bamboo leaves fall.
  // Purely decorative, self-contained, doesn't touch layout.
  var logo = document.querySelector('.pandatechie-logo');
  if (logo) {
    var clicks = 0, clickTimer;
    logo.addEventListener('click', function(e){
      clicks++;
      clearTimeout(clickTimer);
      clickTimer = setTimeout(function(){ clicks = 0; }, 1200);
      if (clicks >= 5) {
        clicks = 0;
        e.preventDefault();
        spawnPandaBurst();
      }
    });
  }

  function spawnPandaBurst(){
    var emojis = ['🐼', '🎋', '🐾'];
    for (var i = 0; i < 24; i++) {
      var span = document.createElement('span');
      span.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      span.style.cssText = [
        'position:fixed', 'top:-40px', 'left:' + (Math.random() * 100) + 'vw',
        'font-size:' + (18 + Math.random() * 20) + 'px',
        'z-index:9999', 'pointer-events:none',
        'transition:transform 2.4s cubic-bezier(.3,.8,.4,1), opacity 2.4s ease'
      ].join(';');
      document.body.appendChild(span);
      requestAnimationFrame(function(el){
        return function(){
          el.style.transform = 'translateY(' + (window.innerHeight + 80) + 'px) rotate(' + (Math.random() * 360) + 'deg)';
          el.style.opacity = '0';
        };
      }(span));
      setTimeout(function(el){ return function(){ el.remove(); }; }(span), 2600);
    }
  }
})();
