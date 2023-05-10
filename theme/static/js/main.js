const navToggler = document.getElementById("navToggler");
const navSm = document.getElementById("navSm");
const navSmContainer = navSm.querySelector(".container");
const hamburger = navToggler.querySelector("#hamburger");
const lineA = hamburger.querySelector('.line_a');
const lineB = hamburger.querySelector('.line_b');
const lineC = hamburger.querySelector('.line_c');
let navOpen = false

navToggler.addEventListener("click", () => {
    let tl1 = gsap.timeline({paused: true, defaults: {duration: .2}})
    let tl2 = gsap.timeline({paused: true, defaults: {duration: .2}})
    
    tl1.to(lineA, {translateY: 12})
    .to(lineC, {translateY: -12}, '-=.2')
    .to(lineB, {scale: 0}, '-=.2')
    .to(lineA, {rotate: 45})
    .to(lineC, {rotate: -45}, '-=.2')
    .to(navSm, {clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', duration: .5}, '-=.2')
    .to(navSmContainer, {translate: '0 0', opacity: 1, duration: .5}, '-=.5')
    
    tl2.to(lineC, {rotate: 0})
    .to(lineA, {rotate: 0}, '-=.2')
    .to(lineB, {scale: 1})
    .to(lineA, {translateY: 0}, '-=.2')
    .to(lineC, {translateY: 0}, '-=.2')
    .to(navSmContainer, {translate: '0 20%', opacity: 0.3, duration: .5}, '-=.2')
    .to(navSm, {clipPath: 'polygon(0 0, 100% 0, 100% 0%, 0 0%)', duration: 0.5}, '-=.3')

    console.log('click');
    console.log(navOpen);
    if (!navOpen) {
        tl1.play()
        tl1.addPause()
        navOpen=!navOpen
    }
    else{
        console.log('here');
        tl2.play()
        navOpen=!navOpen
    }
})

// hiding header and hamburger
let lastScroll = 0;
const header = document.getElementById("navbar-sticky")

window.addEventListener("scroll", () => {
	const currentScroll = window.pageYOffset;
	// console.log(currentScroll);
    // timeline to hide nav and hamburger
    let tlHide = gsap.timeline({paused: true, defaults: {duration: .2, Easings: Expo.EaseOut}})
    .to(header, {top: '-15%',})
    if (navToggler.offsetHeight) // execute if the navToggler has a height (is visible)
        tlHide.to(navToggler, {bottom: '-4rem'})

    let tlShow = gsap.timeline({paused: true, defaults: {duration: .2}})
    .to(header, {top: '0%',})
    if (navToggler.offsetHeight)
        tlShow.to(navToggler, {bottom: '2rem'})

	if (currentScroll <= 0) {
		header.classList.remove("show");
        tlShow.play()
	}
	if (currentScroll > lastScroll && !header.classList.contains("hide")) {
		header.classList.remove("show");
		header.classList.add("hide");
        tlHide.play()
	}
	if (currentScroll < lastScroll && header.classList.contains("hide")) {
		header.classList.remove("hide");
		header.classList.add("show");
        tlShow.play()
	}
	lastScroll = currentScroll;
});

//#region slider
// let slides = document.getElementById('slides').children

// let currentSlide = 1000;
// let nextSlide = 0;

// function slide() {
//    let next = slides[nextSlide]
//    let current = slides[currentSlide]

//    const t1 = gsap.timeline({ paused: true, defaults: { Easings: Expo.EaseOut } })
   
//    if (current) {
//       t1.to(current.querySelector('.fade-in'), { opacity: 0, scale: 0.1, duration: 0.3 })
//          .to(current.querySelector('button'), { opacity: 0, scale: 0.1, duration: 0.4 }, '+=0.1')
//          .to(current, { clipPath: 'polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)' })
//    }
//    t1.fromTo(next, { clipPath: 'polygon(100% 0%, 100% 0%, 100% 100%, 100% 100%)'}, { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', duration: 1 }, '-=1.5')
//       .to(next.querySelector('.fade-in'), { opacity: 1, scale: 1, duration: 0.5 }, '+=0.1')
//       .to(next.querySelector('button'), { opacity: 1, scale: 1, duration: 0.5 }, '+=0.1')
      
   
//    t1.play()
//    // switch next and previous slides
//    switchSlides()
// }

// function switchSlides() {
//    let max = slides.length-1
//    if (nextSlide == max) {
//       currentSlide = nextSlide
//       nextSlide = 0
//    }
//    else {
//       currentSlide = nextSlide
//       nextSlide += 1
//    }
// }

// slide()
// setInterval(slide, 10000)
//#endregion


let carousel = null
let carouselslides = null
let carouselslideLength = null
let carouselcurrentSlide = null

function setCarouselDefaults() {
    carousel = document.getElementById('carouselSlides')
    carouselslides = document.querySelectorAll('#carouselSlides .carouselSlide')
    carouselslideLength = carouselslides.length - 1
    carouselcurrentSlide = -1

    // set the slides initially
    carouselslides.forEach(slide => {
        gsap.set(slide.querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)'
        })
        gsap.set(slide, {
            clipPath: 'polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)'
        })
    });
}

class CarouselSlider {
    // method to show the slide
    static showSlide(num) {
        // showing next slide
        const timeline1 = gsap.timeline({
            paused: true,
            defaults: {
                Easings: Expo.EaseOut
            }
        }).to(carouselslides[carouselcurrentSlide], {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)',
            duration: 0.9
        }, '+=.7').to(carouselslides[carouselcurrentSlide].querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)',
            duration: 0.4,
            stagger: 0.15
        }, '+=.5')
        timeline1.play()
    }
    // method to hide the slide
    static hideSlide(num) {
        // hiding previous slide
        const timeline2 = gsap.timeline({
            paused: true,
            defaults: {
                Easings: Expo.easeInOut
            }
        }).to(carouselslides[carouselcurrentSlide].querySelectorAll('.content > *'), {
            clipPath: 'polygon(0% 0%, 100% 0%, 100% 0%, 0% 0%)',
            duration: 0.4,
            stagger: 0.15
        }).to(carouselslides[carouselcurrentSlide], {
            clipPath: 'polygon(100% 0%, 100% 0%, 100% 100%, 100% 100%)',
            duration: 0.6,
            delay: 2
        }, '+=1')
        timeline2.play()
    }
    static nextSlide() {
        if (carouselcurrentSlide == carouselslideLength) {
            return carouselcurrentSlide = 0
        } else {
            return ++carouselcurrentSlide
        }
    }
    static switchSlides() {
        if (carouselcurrentSlide >= 0) {
            CarouselSlider.hideSlide(carouselcurrentSlide)
            CarouselSlider.showSlide(CarouselSlider.nextSlide())
        }
        else {
            CarouselSlider.showSlide(CarouselSlider.nextSlide())
        }
    }
}

if (homepage) {
    // Carousel.switchSlides()
    setCarouselDefaults()
    CarouselSlider.switchSlides()
    setInterval(CarouselSlider.switchSlides, 20000)
}

//#region ScrollTrigger
gsap.set(".slide-in-top", {
    y: 200,
    clipPath: 'polygon(0 0, 100% 0, 100% 0, 0 0)'
});
gsap.set(".slide-in-top-0", {
    y: 200,
    clipPath: 'polygon(0 0, 100% 0, 100% 0, 0 0)'
});
gsap.set(".slide-in-right", {
    x: -400,
    clipPath: 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)'
});
gsap.set(".slide-in-left", {
    x: 400,
    clipPath: 'polygon(0% 0, 0% 0, 0% 100%, 0% 100%)'
});
gsap.set('.fade-in', {
    opacity: 0,
})
gsap.set('.pop-in', {
    opacity: 0.5,
    scale: 0.2
})


ScrollTrigger.batch('.slide-in-top', {
    onEnter: (batch) => {
        gsap.to(batch, {
            clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
            y: 0,
            stagger: 0.2,
            duration: .7
        })
    },
    start: '100px bottom',
    // markers: true
})

ScrollTrigger.batch('.slide-in-top-0', {
    onEnter: (batch) => {
        gsap.to(batch, {
            clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
            y: 0,
            stagger: 0.2,
            duration: .7
        })
    },
    start: '00px bottom',
    // markers: true
})

ScrollTrigger.batch('.slide-in-right', {
    onEnter: (batch) => {
        gsap.to(batch, {
            clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
            x: 0,
            stagger: 0.2,
            duration: 1
        })
    },
    start: '50% bottom',
    // markers: true
})

ScrollTrigger.batch('.slide-in-left', {
    onEnter: (batch) => {
        gsap.to(batch, {
            clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
            x: 0,
            stagger: 0.2,
            duration: 1
        })
    },
    start: '50% bottom',
    // markers: true
})

ScrollTrigger.batch('.fade-in', {
    onEnter: (batch) => {
        gsap.to(batch, {
            opacity: 1,
            stagger: 0.2,
            duration: 1
        })
    },
    start: '100px bottom',
    // markers: true
})

ScrollTrigger.batch('.pop-in', {
    onEnter: (batch) => {
        gsap.to(batch, {
            opacity: 1,
            scale: 1,
            stagger: 0.2,
            duration: .5
        })
    },
    start: '100px bottom',
    // markers: true
})
// t2.play()
//#endregion