"use strict";(self["webpackChunklego"]=self["webpackChunklego"]||[]).push([[535],{6829:(n,r,e)=>{e.r(r),e.d(r,{default:()=>x});var o=e(821),t=function(n){return(0,o.dD)("data-v-7a33c463"),n=n(),(0,o.Cn)(),n},l={class:"container"},s=t((function(){return(0,o._)("div",{class:"title"},"Neural LEGO",-1)})),a={class:"login-box"},u=t((function(){return(0,o._)("h2",null,"Log in",-1)})),i={method:"POST"},d={class:"input-box"},m=t((function(){return(0,o._)("label",{for:"username",class:"form-label"},"Username",-1)})),c={class:"input-box"},p=t((function(){return(0,o._)("label",{for:"password",class:"form-label"},"Password",-1)})),f={class:"login-btn"},_=t((function(){return(0,o._)("div",{class:"register"},[(0,o._)("p",null,[(0,o._)("a",{href:"/register"},"Register")])],-1)}));function g(n,r,e,t,g,w){return(0,o.wg)(),(0,o.iD)("div",l,[s,(0,o._)("div",a,[u,(0,o._)("form",i,[(0,o._)("div",d,[m,(0,o.wy)((0,o._)("input",{"onUpdate:modelValue":r[0]||(r[0]=function(n){return g.loginForm.email=n}),type:"text",class:"form-control",id:"username",name:"username",required:""},null,512),[[o.nr,g.loginForm.email]])]),(0,o._)("div",c,[p,(0,o.wy)((0,o._)("input",{"onUpdate:modelValue":r[1]||(r[1]=function(n){return g.loginForm.password=n}),type:"password",class:"form-control",id:"password",name:"password",required:""},null,512),[[o.nr,g.loginForm.password]])]),(0,o.wy)((0,o._)("input",{"onUpdate:modelValue":r[2]||(r[2]=function(n){return g.loginForm.next_url=n}),type:"hidden",class:"form-control",id:"next_url",name:"next_url"},null,512),[[o.nr,g.loginForm.next_url]]),(0,o._)("div",f,[(0,o._)("button",{type:"submit",onClick:r[3]||(r[3]=function(r){return n.submitFrom(r)})},"Login")]),_])])])}var w=e(9669),b=e.n(w);const v={name:"LoginView",data:function(){return{loginForm:{username:"",password:"",next_url:"/project"}}},methods:{submitForm:function(n){n.preventDefault(),b()({method:"post",url:"/login/",data:{username:this.loginForm.username,password:this.loginForm.password,next_url:this.loginForm.next_url}})}}};var h=e(3744);const F=(0,h.Z)(v,[["render",g],["__scopeId","data-v-7a33c463"]]),x=F}}]);
//# sourceMappingURL=login.js.map