const menu=document.getElementById('krpng'); //Menu cần click
const hide=document.getElementById('mc'); //Chi tiết menu khi click
const loading=document.getElementById('loading'); //loading đầu ảnh
const main=document.getElementById('ngt'); // main đang ẩn
const me=document.getElementById('me'); // get me
const Qayrermc=document.getElementById('Qayrermc'); // get Qayrermc từ html
const gui=document.getElementById('main')

menu.addEventListener('click', () => {
    if (hide.style.display === 'none') {
        hide.style.display = 'inline-block';
    }
    else {
        hide.style.display = 'none';
    }
}); // ấn để hiện menu
document.addEventListener('click', (event) => {
    if (!hide.contains(event.target) && event.target !== menu) {
      hide.style.display = 'none';
    }
  }); // lắng nghe sự kiện khi k ấn
me.addEventListener('click', () => {
    if (Qayrermc.style.display === 'none') {
        Qayrermc.style.display = 'block';
    }
    else Qayrermc.style.display = 'none';
});
window.addEventListener('load', () => {
    setTimeout(() => {
        loading.style.display = 'none'; 
        gui.style.display = 'block'; 
    }, 2500)
}); // loading