import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel1FlatEven13 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven13 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel1FlatComponentChunk13

end RHP2Bridge
