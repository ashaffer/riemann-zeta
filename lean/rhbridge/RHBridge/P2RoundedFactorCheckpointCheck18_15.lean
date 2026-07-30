import RHBridge.P2RoundedFactorCheckpointData18

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FactorChunk15 :
    P2RoundedFactorCheckpointData.panel18Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨18, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel18Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨18, by decide⟩ := by
  decide +kernel

theorem panel18Prefix60_eq :
    P2RoundedFactorCheckpointData.panel18Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk15.1

theorem panel18Prefix61_eq :
    P2RoundedFactorCheckpointData.panel18Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk15.2.1

theorem panel18Prefix62_eq :
    P2RoundedFactorCheckpointData.panel18Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk15.2.2.1

theorem panel18Prefix63_eq :
    P2RoundedFactorCheckpointData.panel18Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨18, by decide⟩ := by
  exact panel18FactorChunk15.2.2.2

end RHP2Bridge
