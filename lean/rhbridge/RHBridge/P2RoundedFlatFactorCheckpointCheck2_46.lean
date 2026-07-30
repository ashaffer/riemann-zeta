import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel2FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel2FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel2FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel2TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel2FlatComponentChunk46

end RHP2Bridge
