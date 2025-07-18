import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Header from './Components/Header/Header'
import Hero_Section from './Components/Hero-Section/Hero-Section'
import Dishes from './Components/Dishes/Dishes'
import Best_Offers from './Components/Best-Offers/Best_offers'
import Subscribe from './Components/Subscribe/subscribe'
import Choosen_by_you from './Components/Choosen-by-you/Choosen_by_you'
import Review from './Components/Review/review_section'
import Flex_off from './Components/flex-off/flex_off'
import Footer from './Components/footer/footer'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header></Header>
      <Hero_Section></Hero_Section>
      <Dishes></Dishes>
      <Best_Offers></Best_Offers>
      <Subscribe></Subscribe>
      <Choosen_by_you></Choosen_by_you>
      <Review></Review>
      <Flex_off></Flex_off>
      <Footer></Footer>
    </>
  )
}

export default App
