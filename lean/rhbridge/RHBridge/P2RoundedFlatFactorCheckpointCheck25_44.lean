import RHBridge.P2RoundedFlatFactorCheckpointData25

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel25FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel25FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel25FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel25TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel25FlatComponentChunk44

end RHP2Bridge
