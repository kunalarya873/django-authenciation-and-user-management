import { makeStyles } from "@mui/material";
import theme from "./theme";

const useStyles = makeStyles((theme) =>({
example:{
  color: "#fff",
}
}));
export default function Home() {
  const classes = useStyles();
  return (
    <div className={classes.example}>
      <h1>Home Page</h1>
    </div>

  );
}
