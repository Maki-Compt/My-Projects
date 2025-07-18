import styles from "./review.module.css"
import black_girl from "../../assets/Review/ai-generated-portrait-beautiful-african-dark-skin-woman-color-background_858577-1122.avif"
import white_girl from "../../assets/Review/spanish_women.jpg"
import spanish_girl from "../../assets/Review/white_women.avif"

function review() {
    return(<>
        <div className={styles.review}>

            <div className={styles.review_block}>
                <img src={black_girl} alt="" />
                <h3>Carla Matos</h3>
                <p>Eu tive uma ótima experiência com o restaurante, o pessoal é bem simpático e a comida é muito boa, 5 estrelas, não menos.</p>
            </div>
            
            
            <div className={styles.review_block}>
                <img src={white_girl} alt="" />
                <h3>Aricelvia Araújo</h3>
                <p>Honestamente tive um dos momentos mais románticos com o meu marido, graças as delicias que o restaurante ofereceu-nos, muito bom.</p>
            </div>

            <div className={styles.review_block}>
                <img src={spanish_girl} alt="" />
                <h3>Bianca Moniz</h3>
                <p>Uau! Além de ter diversos pratos, o serviço é também de alta qualidade, espero que continuem assim e melhorem muito mais.</p>
            </div>

        </div>
    </>)
}

export default review
