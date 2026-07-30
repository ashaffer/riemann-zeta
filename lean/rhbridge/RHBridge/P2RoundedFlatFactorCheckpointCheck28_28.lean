import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel28FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel28FlatComponentChunk28

end RHP2Bridge
