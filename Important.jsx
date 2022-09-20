// contexで直接データゲット
const LinkContext = React.createContext(context);

const context = () =>{
return(
    <div>
<NavigationBar />
// ... NavigationBar コンポーネントは以下をレンダー ...
<Link href={user.permalink}>
  <LinkContext.Consumer>
  { (context) => {
    <Avatar user={context.user} size={context.avatarSize} />
  }}
  </LinkContext.Consumer>
</Link>
</div>
);}

res = await fetch("https://fake_url.com")
// return true if res exist
if (res.ok){
  await console.log(res.json())
}