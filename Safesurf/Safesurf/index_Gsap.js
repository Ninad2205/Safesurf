const timer = gsap.timeline();

timer.from("nav ul button ", {
  opacity: 0,
  duration: 2,
  y: -20,
});
timer.from("nav ul li ", {
  opacity: 0,
  duration: 2,
  y: -20,
  stagger: 0.5,
});
gsap.from(".hero h1", {
  opacity: 0,
  duration: 2,
  delay: 1,
  y: -50,
});
gsap.from(".hero .to", {
  opacity: 0,
  duration: 2,
  delay: 3,
});
gsap.from(".home .home_containt p", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".home",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".home .home_containt h1", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".home",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".intro .intro_containt .img img", {
  opacity: 0,
  duration: 5,
  y: -100,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".intro .intro_containt .containt h1", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".intro .intro_containt .containt p", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});

gsap.from(".intro .intro_containt .containt h2", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".intro .intro_containt .containt h3", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".intro .intro_containt .containt h5", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".intro",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".types  h1", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".types",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".types .types_containt .type p", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".types",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".types .types_containt .type h3", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".types",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".types .types_containt .type h4", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".types",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".precautions .precautions_containt .containt p", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".precautions",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".precautions .precautions_containt .containt h1", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".precautions",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".precautions .precautions_containt .containt h2", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".precautions",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".precautions .precautions_containt .containt h5", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".precautions",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".precautions .precautions_containt .img img", {
  opacity: 0,
  duration: 5,
  y: 100,
  scrollTrigger: {
    trigger: ".precautions",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".about .about_containt  h1", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".about",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
gsap.from(".about .about_containt  p", {
  opacity: 0,
  duration: 5,
  scrollTrigger: {
    trigger: ".about",
    scroller: "body",
    start: "top 10%",
    end: "top 100%",
    scrub: 4,
  },
});
