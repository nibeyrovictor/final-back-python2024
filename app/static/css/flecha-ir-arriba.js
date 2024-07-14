    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("flecha-arriba").classList.add("mostrar");
      } else {
        document.getElementById("flecha-arriba").classList.remove("mostrar");
      }
    }

    function irArriba() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
