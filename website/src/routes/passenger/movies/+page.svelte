<script>
    import CardCarousel from "../../../components/CardCarousel.svelte";
    import NavBar from "../../../components/NavBar.svelte";

    let cards = [
        { src: "https://m.media-amazon.com/images/I/41DsVUWsCLL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/516V1BUK6xL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://i5.walmartimages.com/seo/Top-Gun-Maverick-Movie-Poster-Quality-Glossy-Print-Photo-Wall-Art-Tom-Cruise-Jennifer-Connelly-Size-24x36_bbb92289-b359-423e-a8fe-6142b188f677.4da7e4af2871002298f4804afb44b955.jpeg" },
        { src: "https://m.media-amazon.com/images/I/71Tpd21hEbL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/91zqGNzwk5L._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/71BgdzmFDAL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://i.pinimg.com/originals/66/bd/9b/66bd9b1f8354a9aa6900dee35bc2a911.jpg" },
        { src: "https://i.etsystatic.com/41716657/r/il/9c990a/4742863548/il_570xN.4742863548_patj.jpg" },
        { src: "https://m.media-amazon.com/images/I/51b6mLCvBuL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/M/MV5BMDJhMGRjN2QtNDUxYy00NGM3LThjNGQtMmZiZTRhNjM4YzUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg" },
        { src: "https://m.media-amazon.com/images/I/91K98RNBBWL.jpg" },
        { src: "https://m.media-amazon.com/images/I/61f1bYNLpKL._AC_UF1000,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/71U8fIXlGHL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/A1M0qlxNo6L.jpg" },
        { src: "https://m.media-amazon.com/images/I/81ZCRFRoXYL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://m.media-amazon.com/images/I/81oON83v4WL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://pbncanvas.com/wp-content/uploads/2022/02/Knives-Out-movie-poster-paint-by-numbers.jpg" },
        { src: "https://m.media-amazon.com/images/I/61c11xwXFjL._AC_UF894,1000_QL80_.jpg" },
        { src: "https://i.ebayimg.com/images/g/qHwAAOSw1Y5dcuMC/s-l1600.jpg" },
    ]
</script>

<div class="card-carousel">
    <NavBar />
    <CardCarousel cards={cards} />
</div>