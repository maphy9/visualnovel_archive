import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import CreateButton from '../../../Utils/CreateButton/CreateButton'
import { SyncLoader } from 'react-spinners';
import { Link } from 'react-router-dom';

const fetchData = async (url, setData) => {
  const method = "GET";
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
  };
  const res = await fetch(url, { method, headers });
  if (res.status !== 200) {
    console.error(`Error: ${res.status}`);
    return;
  }
  const data = await res.json();
  setData(data);
};

function SideWindow() {
  const [randomVisualNovel, setRandomVisualNovel] = useState(null);

  useEffect(() => {
    fetchData('http://127.0.0.1:8000/get_random_visual_novel/', setRandomVisualNovel);
  }, []);

  return (
    <div className={style.window}>
      <CreateButton url="/" label="Create new article" />
      <div className={style.content}>
        {
        randomVisualNovel === null ? <SyncLoader color={"#70ACEB"} size={32} /> :
        <>
        <div className={style.content_name}>Random visual novel</div>
        <div className={style.visual_novel_image}><img src={randomVisualNovel.image} alt="Random visual novel image" /></div>
        <div className={style.visual_novel_title}>{randomVisualNovel.title}</div>
        <div className={style.visual_novel_description}>{randomVisualNovel.description}</div>
        <Link to="/" className={style.article_link}><div>See more</div></Link>
        </>
        }
      </div>
    </div>
  )
}

export default SideWindow