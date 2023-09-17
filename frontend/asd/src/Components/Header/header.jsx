import logoIMG from "./../../Img/logo-no-background.svg"
import searchIMG from  "./../../Img/search.svg"
import basketIMG from "./../../Img/Basket.svg"
import ProfileIMG from "./../../Img/Profile.svg"
import favoritesIMG from  "./../../Img/favorites.svg"
import "./style_header.css"
import { Link } from "react-router-dom"



function Header(){
    return (
        <header>
        <Link to = "/"><img class="logo"src={logoIMG} alt=""/></Link>
        <div>
        <form action="" method="get">
            <input type="search" placeholder="ПОИСК"/>
            <button type="submit"><img src={searchIMG} alt=""/></button>
        </form>
    </div>
        <div class="profile-nav">   
            <ul>
                <li>
                    <img src={favoritesIMG} alt=""/>
                    <p>Избранное</p>

                </li>
                <li>
                    <img src={basketIMG} alt=""/>
                    <p>Корзина</p>
                </li>
                <li>
                    <Link to = "sign_up">
                        <img src={ProfileIMG} alt=""/>
                        <p>Войти</p>
                    </Link>
                </li>
            </ul>
        </div>
    </header>
    );
}


export default Header;