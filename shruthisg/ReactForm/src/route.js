import Home from './Views/home.js'
import SearchQP from './Views/searchQP.js'
import SearchBook from './Views/SearchBook.js'
import TemplateQP from './Views/templateQP.js'
import Projects from './Views/projects.js'
import Contributors from './Views/contributors.js'
import Contact from './Views/contact.js'

const Routes = [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/searchQP",
      name: "searchQP",
      component: SearchQP
    },
    {
      path: "/books",
      name: "searchBook",
      component: SearchBook
    },
    {
      path: "/templateQP",
      name: "templateQP",
      component: TemplateQP
    },
    {
      path: "/projects",
      name: "projects",
      component: Projects
    },
    {
      path: "/contributors",
      name: "Contributors",
      component: Contributors
    },
    {
      path: "/contact",
      name: "Contact",
      component: Contact
    }
  ];
  
export default Routes;