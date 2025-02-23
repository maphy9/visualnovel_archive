import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import CreateButton from '../../../Utils/CreateButton/CreateButton'
import { SyncLoader } from 'react-spinners';
import { Link } from 'react-router-dom';
import Users from './Users/Users';

const fetchData = async (url, setData) => {
  const method = "POST";
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
  };
  const body = JSON.stringify({ page_size: 6, page_number: 1 });
  const res = await fetch(url, { method, headers, body });
  if (res.status !== 200) {
    console.error(`Error: ${res.status}`);
    return;
  }
  const data = await res.json();
  setData(data);
};

function SideWindow() {
  const [mostActiveUsers, setMostActiveUsers] = useState(null);

  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_most_active_users/', setMostActiveUsers);
  }, []);

  return (
    <div className={style.window}>
      <CreateButton url="/" label="Create new discussion" />
      <div className={style.content}>
        {
        mostActiveUsers === null ? <SyncLoader color={"#70ACEB"} size={32} /> :
        <>
        <div className={style.content_name}>Most active users</div>
        <Users users={mostActiveUsers} />
        <Link to="/" className={style.users_link}><div>See more</div></Link>
        </>
        }
      </div>
    </div>
  )
}

export default SideWindow