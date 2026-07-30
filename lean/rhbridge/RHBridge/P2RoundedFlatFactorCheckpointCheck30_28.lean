import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel30FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel30FlatComponentChunk28

end RHP2Bridge
