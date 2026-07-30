import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel11FlatEven12 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven12 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel11FlatComponentChunk12

end RHP2Bridge
