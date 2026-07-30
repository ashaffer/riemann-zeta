import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk46 :
    P2RoundedFactorCheckpointData.panel30FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd22_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd22 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨22, by decide⟩ := by
  exact panel30FlatComponentChunk46

end RHP2Bridge
