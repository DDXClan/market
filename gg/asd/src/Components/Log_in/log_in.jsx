import { Link } from 'react-router-dom';
import React, { useState } from 'react';
import './style_login.css'
const Log_in = () => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');

  const handleLoginChange = (event) => {
    setLogin(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Отправка данных авторизации на сервер
    const data = {
      username: login,
      password: password,
    };

    fetch('http://26.8.118.81:8000/user/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        // Обработка успешной авторизации
      })
      .catch((error) => {
        // Обработка ошибок
      });
  };

  return (
    <div class="reg_main">
      <h1>Войти</h1>
      <h2>Нет аккаунта? <Link to="/sign_up" replace>Зарегистрироваться</Link></h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={login} onChange={handleLoginChange} placeholder="Login" />
        <input type="password" value={password} onChange={handlePasswordChange} placeholder="Password" />
        <button type="submit">Войти</button>
      </form>
    </div>
  );
};

export default Log_in;