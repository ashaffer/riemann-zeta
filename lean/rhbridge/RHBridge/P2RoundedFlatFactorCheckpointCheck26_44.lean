import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel26FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel26FlatComponentChunk44

end RHP2Bridge
