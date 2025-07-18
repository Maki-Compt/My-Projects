import styles from "./Hero_section.module.css"

function Hero_Section() {
    return(<>
        <div className={styles.hero_section}>
            <div className={styles.opac_bg}></div>
            <div className={styles.hero_section_display_tag}>
                <h1>Descubra diveros sabores que o nosso restaurante tem pra oferecer, desde pratos locais até aos mais exóticos</h1>
                <button>Saiba mais</button>
            </div>
        </div>
    </>)
}

export default Hero_Section