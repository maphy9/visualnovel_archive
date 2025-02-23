import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import Choice from '../../../Utils/Choice/Choice'
import { SyncLoader } from 'react-spinners';
import Articles from './Articles/Articles';
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
  const [popularArticles, setPopularArticles] = useState(null);
  const [newArticles, setNewArticles] = useState(null);
  const [mostLikedArticles, setMostLikedArticles] = useState(null);

  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_popular_visual_novels/', setPopularArticles);
  }, []);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_new_visual_novels/', setNewArticles);
  }, []);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_most_liked_visual_novels/', setMostLikedArticles);
  }, []);

  return (
    <div className={style.window}>
      <div className={style.choices}>
        <Choice type={type} setType={setType} ownType={"Popular"} label={"articles"} />
        <Choice type={type} setType={setType} ownType={"New"} label={"articles"} />
        <Choice type={type} setType={setType} ownType={"Most liked"} label={"articles"} />
      </div>
      <div className={style.content}>
        {(() => {
          let articles = null;
          if (type === "Popular" && popularArticles !== null) {
            articles = popularArticles;
          } else if (type === "New" && newArticles !== null) {
            articles = newArticles;
          } else if (type === "Most liked" && mostLikedArticles !== null) {
            articles = mostLikedArticles;
          }

          if (articles !== null) {
            return <>
            <Articles articles={articles} />
            <Link className={style.articles_link} to="/"><div>See more</div></Link>
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