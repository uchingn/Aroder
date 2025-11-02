
//  home page 
/* 
do you want changeing language bangla to englist 

so insert name ='' and data-i18n=''


for example :::::::    data-i18n="profile"


and write 
en: 
bn:


*/


   
  const translations = {
    en: { 
      logoText:"Efarmers", 
      searchInput:"Search for products, buyers, or exchanges", 
      home:"Home", 
      categories:"Categories", 
      help:"Help", 
      profile:"Profile",
      Activitystatus:"Your Activity Status", 
      search: "Search for products, buyers, or exchanges",
    },
    bn: { 
      logoText:"ইফার্মারস", 
      searchInput:"প্রোডাক্ট, ক্রেতা অথবা এক্সচেঞ্জ খুঁজুন", 
      home:"হোম", 
      categories:"ক্যাটাগরি", 
      help:"সাহায্য", 
      profile:"প্রোফাইল", 
      Activitystatus:"আপনার কার্যকলাপের অবস্থা", 
      search: "প্রোডাক্ট, ক্রেতা অথবা এক্সচেঞ্জ খুঁজুন",
    }
  };

  let currentLang = "en";

  // Language toggle
  const langToggleBtn = document.getElementById("langToggle");
  langToggleBtn.addEventListener("click", () => {
    currentLang = currentLang === "en" ? "bn" : "en";
    const dict = translations[currentLang];

    // Update elements with IDs
    for (const key in dict) {
      const el = document.getElementById(key);
      if (el) el.textContent = dict[key];
    }

    // Update elements with data-i18n
    document.querySelectorAll("[data-i18n]").forEach(el => {
      const key = el.getAttribute("data-i18n");
      if (dict[key]) {
        if (el.tagName === "INPUT") {
          el.setAttribute("placeholder", dict[key]);
        } else {
          el.textContent = dict[key];
        }
      }
    });

    langToggleBtn.textContent = currentLang === "en" ? "বাংলা" : "English";
  });

  // Profile dropdown toggle
  const profileToggle = document.getElementById('profileToggle');
  const profileDropdown = document.getElementById('profileDropdown');

  profileToggle.addEventListener('click', (e) => {
    e.preventDefault();
    profileDropdown.classList.toggle('hidden');
  });

  window.addEventListener('click', e => {
    if(!profileToggle.contains(e.target) && !profileDropdown.contains(e.target)) {
      profileDropdown.classList.add('hidden');
    }
  });

  // Mobile menu toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const menuItems = document.getElementById('menu-items');
  const menuIcon = document.getElementById('menuIcon');

  mobileBtn.addEventListener('click', () => {
    menuItems.classList.toggle('hidden');

    // Toggle icon bars/times
    menuIcon.classList.toggle('fa-bars');
    menuIcon.classList.toggle('fa-times');
  });

  // Ensure desktop menu shows correctly on resize
  window.addEventListener('resize', () => {
    if(window.innerWidth >= 768) { // md breakpoint
      menuItems.classList.remove('hidden');
      menuIcon.classList.add('fa-bars');
      menuIcon.classList.remove('fa-times');
    } else {
      menuItems.classList.add('hidden');
    }
  });
 

   
  const toggleBtn = document.getElementById("theme-toggle");
  const icon = document.getElementById("theme-icon");
  const body = document.body;

  toggleBtn.addEventListener("click", (e) => {
    e.preventDefault();

    // Toggle dark mode class on <body>
    body.classList.toggle("dark-mode");

    // Switch icon
    if (body.classList.contains("dark-mode")) {
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
      body.style.backgroundColor = "#1f2937"; // Tailwind gray-800
      body.style.color = "#f9fafb"; // text-gray-50
    } else {
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
      body.style.backgroundColor = "#f0fdfa"; // light green
      body.style.color = "#111827"; // text-gray-900
    }
  });
 

   
 const likeBtn = document.getElementById('likeBtn');
const likeIcon = likeBtn.querySelector('i');

likeBtn.addEventListener('click', function(e) {
  e.preventDefault();

  // Toggle red color
  likeIcon.classList.toggle('text-red-500');

  // Add pop animation
  likeIcon.classList.add('heart-pop');
  setTimeout(() => {
    likeIcon.classList.remove('heart-pop');
  }, 3000);
});
document.getElementById('notification-count').textContent = 5;

//  home page end//////////////////////////////////////////////////////////////////////////////////


// hear button colors set  ///////////////////////////////////////////////////////////////////

const likeBtns = document.getElementById('likeBtn');
const likeIcons = likeBtn.querySelector('i');

likeBtns.addEventListener('click', function(e) {
  e.preventDefault();

  // Toggle red color
  likeIcons.classList.toggle('text-red-500');

  // Add pop animation
  likeIcons.classList.add('heart-pop');
  setTimeout(() => {
    likeIcons.classList.remove('heart-pop');
  }, 300);
});

// hear icon color set end ?//////////




// //   register password validetion erro show  start    // ///////////////////
 function toggleVisibility(toggleBtnId, inputId) {
        const toggleBtn = document.getElementById(toggleBtnId);
        const input = document.getElementById(inputId);

        toggleBtn.addEventListener('click', () => {
            const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
            input.setAttribute('type', type);
            toggleBtn.innerHTML = type === 'password' ? '<i class="fa-solid fa-eye"></i>' : '<i class="fa-solid fa-eye-slash"></i>';
        });
    }

    toggleVisibility('togglePassword', 'password');
    toggleVisibility('toggleConfirmPassword', 'confirm-password');

    
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    const passwordError = document.getElementById('passwordError');

    function checkPasswordMatch() {
        if (confirmPassword.value && password.value !== confirmPassword.value) {
            passwordError.classList.remove('hidden');
        } else {
            passwordError.classList.add('hidden');
        }
    }

    password.addEventListener('input', checkPasswordMatch);
    confirmPassword.addEventListener('input', checkPasswordMatch);




//   register password validetion erro show  start    // ///////////////////


// product entry page password vlidetion ///////////////////////////////


function previewImage(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    if(input.files && input.files[0]) {
      const reader = new FileReader();
      reader.onload = function(e) {
        preview.src = e.target.result;
        preview.classList.remove('hidden');
      }
      reader.readAsDataURL(input.files[0]);
    }
  }

// product entry end ???????????????????????????????????????????????????????????  



 // password togole login page start ???????????????????????????????????????????????????????????
 
  const togglePassword = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('password');
  const eyeIcon = document.getElementById('eyeIcon');

  togglePassword.addEventListener('click', () => {
    const isPassword = passwordInput.type === 'password';
    passwordInput.type = isPassword ? 'text' : 'password';
    eyeIcon.classList.toggle('fa-eye');
    eyeIcon.classList.toggle('fa-eye-slash');
  });
 
 
    const forgotPasswordLink = document.getElementById('forgot_password');
    const recoveryLink = document.getElementById('recovery');
    
    forgotPasswordLink.addEventListener('click', (e) => {
        e.preventDefault();
        if (forgotPasswordLink.classList.contains('hidden')) {
            return;
        }else{
            recoveryLink.addEventListener('click', (e) => {
                e.preventDefault();
                 recoveryLink.textContent = "যোগাযোগ করুন: 01865650309 ";
               })
        }
        forgotPasswordLink.classList.add('hidden');
        recoveryLink.classList.remove('hidden');

    });



    // login page //////////////////////////////////////////////////////////////////////////////////
 