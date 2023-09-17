import favoritesIMG from  "./../../Img/favorites.svg"
import basketIMG from "./../../Img/Basket.svg"
// import fludIMG from "./../../icon_main/Flud.svg"
import "./style_cards.css"
import {Link } from 'react-router-dom';
import { useState, useEffect } from "react";
const Cards = () => {
    const [cards, setCards] = useState([]);
    useEffect(() =>{
        fetch('http://26.8.118.81:8000/item/all')
            .then(res => res.json())
            .then(data => setCards(data))
    }, []);
    
    return ( 
        
        <>
        <div class = "Card_Product">
            <ul>
                {
                    cards.map(card => (
                        <li>
                            <img key ={card.img} class ="product_img" src={`/tovar_image/${card.img}`}/>
                            <Link key={card.id} to ={`/item/${card.id}`}><p key={card.product_name} class = "product_name">{card.product_name}</p></Link>
                            <div class="product_menu">
                                <Link key={card.id} to={`/item/${card.id}`}><p key={card.cost}>{card.cost}</p></Link>
                                <img src={favoritesIMG}/>
                                <img src={basketIMG}/>  
                            </div>
                        </li>
                    ))
                }
            </ul>
        </div> 
        </>
     );
}
 
export default Cards;