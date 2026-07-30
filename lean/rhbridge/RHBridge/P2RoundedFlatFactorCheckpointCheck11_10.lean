import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel11FlatEven10 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven10 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel11FlatComponentChunk10

end RHP2Bridge
