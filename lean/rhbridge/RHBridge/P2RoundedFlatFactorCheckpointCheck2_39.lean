import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel2FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel2FlatComponentChunk39

end RHP2Bridge
