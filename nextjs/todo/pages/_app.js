import { useState } from 'react';
import 'antd/dist/antd.css';
import '../styles/global.css'
import 'animate.css'
import 'antd/dist/antd.variable.min.css';
import { ConfigProvider } from 'antd';
import { Hydrate, QueryClient, QueryClientProvider } from 'react-query'



ConfigProvider.config({
  theme: {
    primaryColor: '#05595B',
    borderRadiusBase : "20px",
  },
});


function MyApp({ Component, pageProps }) {
  const [queryClient] = useState(() => new QueryClient())

  return(
    <ConfigProvider direction="rtl">
      <QueryClientProvider client={queryClient}>
        <Hydrate state={pageProps.dehydratedState}>
          <Component {...pageProps} />
        </Hydrate>
      </QueryClientProvider>
    </ConfigProvider>
  )
}

export default MyApp
