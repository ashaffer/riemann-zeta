import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel28FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel28FlatComponentChunk30

end RHP2Bridge
