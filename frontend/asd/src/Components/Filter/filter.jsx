import fridgeIMG from  "./../../icon_main/Fridge.svg"
import pcIMG from "./../../icon_main/PC.svg"
import platesIMG from "./../../icon_main/Plates.svg"
import WMIMG from  "./../../icon_main/WashingMachine.svg"
import "./style_filter.css"
const Filter = () => {
    return (  
        <div Nameclass="Filtr">
            <div class = "Category" id="hueta2">
                <ul>
                    <li class = "hueta">
                        <img src={fridgeIMG}/>
                        <p>Холодильники</p>
                    </li>
                    <li>
                        <img src={pcIMG}/>
                        <p>Плиты</p>
                    </li>
                    <li>
                        <img src={platesIMG}/>
                        <p>Стиральные машины</p>
                    </li>
                    <li>
                        <img src={WMIMG}/>
                        <p>Компьютеры</p>
                    </li>
                </ul>
            </div>
        </div>
    );
}
 
export default Filter;

