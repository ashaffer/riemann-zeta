import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel11FlatEven22 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven22 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel11FlatComponentChunk22

end RHP2Bridge
