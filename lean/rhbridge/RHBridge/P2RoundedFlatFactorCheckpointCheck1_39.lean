import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel1FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel1FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel1FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel1TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel1FlatComponentChunk39

end RHP2Bridge
