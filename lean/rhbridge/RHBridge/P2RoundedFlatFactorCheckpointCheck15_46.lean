import RHBridge.P2RoundedFlatFactorCheckpointData15

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel15FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel15FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel15FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel15TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel15FlatComponentChunk46

end RHP2Bridge
