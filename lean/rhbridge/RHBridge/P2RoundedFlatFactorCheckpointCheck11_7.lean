import RHBridge.P2RoundedFlatFactorCheckpointData11

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11FlatComponentChunk7 :
    P2RoundedFactorCheckpointData.panel11FlatEven7 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel11FlatEven7_eq :
    P2RoundedFactorCheckpointData.panel11FlatEven7 =
      (P2RoundedFactorCheckpointData.panel11TruncatedEvenComponents).get ⟨7, by decide⟩ := by
  exact panel11FlatComponentChunk7

end RHP2Bridge
