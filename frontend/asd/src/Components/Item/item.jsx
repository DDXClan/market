import './style_item.css'
import {Link } from 'react-router-dom'
import { useParams } from 'react-router-dom';
import { useState, useEffect } from "react";

const Item = () => {
    const {id} = useParams(); 
    const [item, setItem] = useState([]);
    useEffect(() =>{
        fetch(`http://26.8.118.81:8000/item/${id}`)
            .then(res => res.json())
            .then(data => setItem(data))
    }, []);
    return ( 
        <>
        <Link to="/"><p class="back_link" >Вернуться к каталогу</p></Link>
        <div class="product_main">  
            <div class = "tovar">
            <img src={`/tovar_image/${item.img}`}/>
                <h2>{item.product_name}</h2>
            </div>
            <div class = "Desription">
                <h4>Описание:</h4>
                <p>{item.description}</p>
            </div>
            <h4 class="Desription-category">{item.category_name}</h4>
            <div class="sell">
                <div class="buy">
                    <h4>Купить</h4>
                    <p>{item.cost}</p>
                </div>
                <h4>Избранное</h4>
            </div>
        </div>
        </>
     );
}
export default Item;
