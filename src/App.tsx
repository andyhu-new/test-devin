import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { ScrollArea } from "@/components/ui/scroll-area"
import { Cloud, Database, Bot, BarChart } from "lucide-react"

function App() {
  return (
    <div className="min-h-screen bg-slate-50 p-8">
      <div className="mx-auto max-w-6xl">
        <header className="mb-12 text-center">
          <h1 className="text-5xl font-bold text-slate-900 mb-4">AWS re:Invent 2023 Highlights</h1>
          <p className="text-lg text-slate-600">Latest announcements and features from AWS</p>
        </header>

        <Tabs defaultValue="genai" className="space-y-6">
          <TabsList className="grid w-full grid-cols-4 bg-slate-100 p-1">
            <TabsTrigger value="genai" className="space-x-2 data-[state=active]:bg-white data-[state=active]:text-slate-900">
              <Bot className="h-5 w-5" />
              <span>Generative AI</span>
            </TabsTrigger>
            <TabsTrigger value="analytics" className="space-x-2 data-[state=active]:bg-white data-[state=active]:text-slate-900">
              <BarChart className="h-5 w-5" />
              <span>Analytics</span>
            </TabsTrigger>
            <TabsTrigger value="compute" className="space-x-2 data-[state=active]:bg-white data-[state=active]:text-slate-900">
              <Cloud className="h-5 w-5" />
              <span>Compute</span>
            </TabsTrigger>
            <TabsTrigger value="database" className="space-x-2 data-[state=active]:bg-white data-[state=active]:text-slate-900">
              <Database className="h-5 w-5" />
              <span>Database</span>
            </TabsTrigger>
          </TabsList>

          <TabsContent value="genai">
            <ScrollArea className="h-96 rounded-lg border border-slate-200 p-6 shadow-sm">
              <div className="grid gap-6">
                <Card className="border-slate-200">
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-2xl font-bold text-slate-900">Amazon Q and Bedrock Updates</CardTitle>
                    <CardDescription className="text-base text-slate-600">Enhanced AI capabilities and new model access</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc pl-8 space-y-3 text-slate-700">
                      <li>Introduction of Amazon Q - A new generative AI-powered assistant</li>
                      <li>Access to Anthropic's Claude 2.1 with 200k token context window</li>
                      <li>New Amazon Titan Image Generator and Multimodal Embeddings</li>
                      <li>Improved model evaluation and comparison tools in Bedrock</li>
                    </ul>
                  </CardContent>
                </Card>

                <Card className="border-slate-200">
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-2xl font-bold text-slate-900">SageMaker Enhancements</CardTitle>
                    <CardDescription className="text-base text-slate-600">Advanced ML development and deployment features</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc pl-8 space-y-3 text-slate-700">
                      <li>New web-based interface with Code Editor and flexible workspaces</li>
                      <li>Introduction of SageMaker HyperPod for distributed training</li>
                      <li>Natural language data exploration in SageMaker Canvas</li>
                      <li>New inference capabilities for cost and latency optimization</li>
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </ScrollArea>
          </TabsContent>

          <TabsContent value="analytics">
            <ScrollArea className="h-96 rounded-lg border border-slate-200 p-6 shadow-sm">
              <div className="grid gap-6">
                <Card className="border-slate-200">
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-2xl font-bold text-slate-900">Amazon Redshift Innovations</CardTitle>
                    <CardDescription className="text-base text-slate-600">Enhanced query and scaling capabilities</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc pl-8 space-y-3 text-slate-700">
                      <li>Amazon Q Generative SQL for natural language query creation</li>
                      <li>AI-driven scaling in Amazon Redshift Serverless</li>
                      <li>Zero-ETL integration with Aurora PostgreSQL</li>
                      <li>Automated workload optimization and management</li>
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </ScrollArea>
          </TabsContent>

          <TabsContent value="compute">
            <ScrollArea className="h-96 rounded-lg border border-slate-200 p-6 shadow-sm">
              <div className="grid gap-6">
                <Card className="border-slate-200">
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-2xl font-bold text-slate-900">Compute and Infrastructure Updates</CardTitle>
                    <CardDescription className="text-base text-slate-600">New instance types and performance improvements</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc pl-8 space-y-3 text-slate-700">
                      <li>AWS Trainium2 instances for AI/ML workloads</li>
                      <li>Enhanced EC2 instance types for improved performance</li>
                      <li>Cross-region data replication for Amazon WorkSpaces</li>
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </ScrollArea>
          </TabsContent>

          <TabsContent value="database">
            <ScrollArea className="h-96 rounded-lg border border-slate-200 p-6 shadow-sm">
              <div className="grid gap-6">
                <Card className="border-slate-200">
                  <CardHeader className="space-y-2">
                    <CardTitle className="text-2xl font-bold text-slate-900">Database Services</CardTitle>
                    <CardDescription className="text-base text-slate-600">Improved integration and analytics capabilities</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <ul className="list-disc pl-8 space-y-3 text-slate-700">
                      <li>Zero-ETL integrations between various AWS database services</li>
                      <li>Enhanced performance optimizations for Aurora</li>
                      <li>Improved analytics capabilities for DynamoDB</li>
                    </ul>
                  </CardContent>
                </Card>
              </div>
            </ScrollArea>
          </TabsContent>
        </Tabs>
      </div>
    </div>
  )
}

export default App
