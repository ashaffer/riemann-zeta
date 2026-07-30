import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk5 :
    P2RoundedFactorCheckpointData.panel1FlatEven5 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven5_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven5 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨5, by decide⟩ := by
  exact panel1FlatComponentChunk5

end RHP2Bridge
