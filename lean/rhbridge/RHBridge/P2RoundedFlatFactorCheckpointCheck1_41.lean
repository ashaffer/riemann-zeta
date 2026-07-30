import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel1FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel1FlatComponentChunk41

end RHP2Bridge
