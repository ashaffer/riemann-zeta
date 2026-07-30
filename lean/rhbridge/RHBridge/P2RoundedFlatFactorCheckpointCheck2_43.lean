import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel2FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel2FlatComponentChunk43

end RHP2Bridge
