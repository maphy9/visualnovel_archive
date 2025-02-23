import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import Choice from '../../../Utils/Choice/Choice';
import { SyncLoader } from 'react-spinners';
import Discussions from './Discussions/Discussions';
import { Link } from 'react-router-dom';

const fetchData = async (url, setData) => {
  const method = "POST";
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
  };
  const body = JSON.stringify({ page_size: 4, page_number: 1 });
  const res = await fetch(url, { method, headers, body });
  if (res.status !== 200) {
    console.error(`Error: ${res.status}`);
    return;
  }
  const data = await res.json();
  setData(data);
};

function MainWindow() {
  const [type, setType] = useState("Popular");
  const [popularDiscussions, setPopularDiscussions] = useState(null);
  const [newDiscussions, setNewDiscussions] = useState(null);
  const [mostRepledToDiscussions, setMostRepledToDiscussions] = useState(null);

  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_popular_discussions/', setPopularDiscussions);
  }, []);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_new_discussions/', setNewDiscussions);
  }, []);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_most_replied_to_discussions/', setMostRepledToDiscussions);
  }, []);

  return (
    <div className={style.window}>
      <div className={style.choices}>
        <Choice type={type} setType={setType} ownType={"Popular"} label={"discussions"} />
        <Choice type={type} setType={setType} ownType={"New"} label={"discussions"} />
        <Choice type={type} setType={setType} ownType={"Most replied to"} label={"discussions"} />
      </div>
      <div className={style.content}>
        {(() => {
          let discussions = null;
          if (type === "Popular" && popularDiscussions !== null) {
            discussions = popularDiscussions;
          } else if (type === "New" && newDiscussions !== null) {
            discussions = newDiscussions;
          } else if (type === "Most replied to" && mostRepledToDiscussions !== null) {
            discussions = mostRepledToDiscussions;
          }

          if (discussions !== null) {
            return <>
            <Discussions discussions={discussions} />
            <Link className={style.discussions_link} to="/"><div>See more</div></Link>
            </>
          } else {
            return <SyncLoader color={"#70ACEB"} size={32} />
          }
        })()}
      </div>
    </div>
  )
}

export default MainWindow