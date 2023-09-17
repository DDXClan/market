
import './reset.css';
import './App.css';
import Header from './Components/Header/header';
import Filter from './Components/Filter/filter';
import Cards from './Components/Cards/cards';
import Footer from './Components/Footer/footer';
import {Routes, Route, Link } from 'react-router-dom';
import Item from "./Components/Item/item";
import Sign_up from './Components/sign_up/sign';
import Log_in from './Components/Log_in/log_in';

function App() {
  return (
    <>
    <Header/>
    <Routes>
      <Route path='/' element={
      <div class='main-main'>
        <Filter/>
        <Cards/>
      </div>} />
      <Route path="/item/:id" element={<Item />}/>
      <Route path='/sign_up' element={<Sign_up />}/>
      <Route path='/log_in' element={<Log_in/>}/>
    </Routes>
    
    <Footer/>
    
    </>
  );
}

export default App;
