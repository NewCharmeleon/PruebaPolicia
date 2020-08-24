//Contenedor y Ejercicios
const fila = document.querySelector('.contenedor-carrusel');
const ejercicios = document.querySelectorAll('.ejercicio');
//Flechas de Carrousel
const flechaIzquierda = document.getElementById('flecha-izquierda');
const flechaDerecha = document.getElementById('flecha-derecha');
//Tipos de Ejercicios
//const listaEjercicios = document.querySelector('.TPlayerNv');
//const tipoEjercicios = document.querySelectorAll('.Button.STPB');
//const tipoEjercicioElegido = document.querySelectorAll('.Button.STPb.Current');
//Ejercicios
const ejercicio = document.querySelector('.Season-EpisodesCn');
const ejercicioElegido = document.querySelectorAll('.owl-item-active');


//?----------Event Listener para la flecha derecha -------------------
/*flechaDerecha.addEventListener('click', ()=> {
    //si probamos por consola con un scroll X en css
    //document.querySelector('.contenedor-carousel).scrollLeft nos da los px 
    //que se corre dicho scroll
    //document.querySelector('.contenedor-carousel).offsetWidht 
    //nos da el ancho total del carousel 
    fila.scrollLeft += fila.offsetWidth ; 

    //guardaremos el indicador activo
    const indicadorActivo = document.querySelector('.indicadores .activo');
    //preguntamos si tiene un elemento a la derecha
    if(indicadorActivo.nextSibling){
        //le agregamos activo al siguiente elemento
        indicadorActivo.nextSibling.classList.add('activo');
        //le removemos activo al indicador activo
        indicadorActivo.classList.remove('activo');
    }
});*/

/*flechaIzquierda.addEventListener('click', ()=> {
    //si probamos por consola con un scroll X en css
    //document.querySelector('.contenedor-carousel).scrollLeft nos da los px 
    //que se corre dicho scroll
    //document.querySelector('.contenedor-carousel).offsetWidht 
    //nos da el ancho total del carousel 
    fila.scrollLeft -= fila.offsetWidth;
    
    //guardaremos el indicador activo
    const indicadorActivo = document.querySelector('.indicadores .activo');
    //preguntamos si tiene un elemento a la derecha
    if(indicadorActivo.previousSibling){
        //le agregamos activo al siguiente elemento
        indicadorActivo.previousSibling.classList.add('activo');
        //le removemos activo al indicador activo
        indicadorActivo.classList.remove('activo');
    }

});*/
//?----------Paginacion -------------------
//redondearemos hacia arriba la division
const numeroPaginas = Math.ceil(ejercicios.length / 5);

//agregamos el ciclo de paginacion
for(let i = 0; i < numeroPaginas; i++){
    //creamos un boton
    const indicador = document.createElement('button');
    //si es el primero lo seteamos a activo
    if(i === 0){
        indicador.classList.add('activo');
    }
    //agregamos al div indicadores el boton creado
    document.querySelector('.indicadores').appendChild(indicador);
    
    //agregamos un EventListener al boton ya agregado al Html
    //para agregarle la posicion en px
    indicador.addEventListener('click', (e)=>{
        fila.scrollLeft = i * fila.offsetWidth;
        //le desagregamos el activo al boton seleccionado
        document.querySelector('.indicadores .activo').classList.remove('activo');
        //le agregamos al activo al boton seleccionado
        e.target.classList.add('activo');
    });

};

//?---------- Hover -------------------
ejercicios.forEach((ejercicio) => {
    ejercicio.addEventListener('mouseenter', (e) => {
        //obtenemos el elemento que activo el evento
        const elemento = e.currentTarget;
        setTimeout(() => {
            //por cada ejercicio ejecuta este codigo
            ejercicios.forEach(ejercicio => ejercicio.classList.remove('.hover'));
            elemento.classList.add('hover');
        }, 200);
    });
});
//?------------- Salida del Hover --------------------------
/*fila.addEventListener('mouseleave', () => {
    ejercicios.forEach(ejercicio => ejercicio.classList.remove('hover'));
});*/
//?------------- 
//Tipos de Ejercicios
const listaEjercicios = document.querySelector('.TPlayerNv');
const tiposEjercicios = document.querySelectorAll('.Button.STPb');
const tipoEjercicioElegido = document.querySelectorAll('.Button.STPb.Current');
const listaEjerciciosReproductor = document.querySelectorAll('.TPlayerTb');
const ejerciciosReproductor = document.querySelectorAll('.owl-item');
//alert(ejerciciosReproductor);


tiposEjercicios.forEach((tipoEjercicios) => {
    tipoEjercicios.addEventListener('click', (e) => {
        //elemento que activo el event
        var elemento = e.currentTarget;
        var video = elemento.dataset.tplayernv;
        //alert(video);
        var videoReproductor = document.getElementById(video);
       // alert(videoReproductor);

        setTimeout(() => {
            //Botonera
            tiposEjercicios.forEach(
                tipoEjercicios => tipoEjercicios.classList.remove('Current')
            );
            elemento.classList.add('Current');
            //Reproductor
            listaEjerciciosReproductor.forEach(
                videoReproductor => videoReproductor.classList.remove('Current')
            );
            //Carousel
            videoReproductor.classList.add('Current');
            //video="";
       


           }, 100);
    });
});


ejerciciosReproductor.forEach((ejercicioReproductor) => {
    
    ejercicioReproductor.addEventListener('click', (e) => {
        
        
        //elemento que activo el event
        const elemento = e.currentTarget;
       //alert(elemento);
       // const video = elemento.siblings.dataset.tplayernv;
       //const video = elemento.innerHTML;
       const video = (e.currentTarget.getElementsByClassName('TPostMv'))[0].dataset.tplayernv;
       //const video3= 1//video2[0].dataset.tplayernv;
        //alert(elemento);
        //alert(video);
        //alert(video2);
       //alert(video3);
        const videoReproductor = document.getElementById(video);

        setTimeout(() => {
            //carousel
            ejerciciosReproductor.forEach(
                ejercicioReproductor => ejercicioReproductor.classList.remove('active-light')
                
            );
            //alert("alkdjflkdjsa");
            elemento.classList.add('active-light');
            //Reproductor
            listaEjerciciosReproductor.forEach(
                videoReproductor => videoReproductor.classList.remove('Current')
            );
            //Reproductor
            videoReproductor.classList.add('Current');
           // alert("alkdjflkdjsa");
       


           }, 100);
    });
});

