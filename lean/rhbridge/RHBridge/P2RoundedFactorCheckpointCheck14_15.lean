import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk15 :
    P2RoundedFactorCheckpointData.panel14Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix60_eq :
    P2RoundedFactorCheckpointData.panel14Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk15.1

theorem panel14Prefix61_eq :
    P2RoundedFactorCheckpointData.panel14Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk15.2.1

theorem panel14Prefix62_eq :
    P2RoundedFactorCheckpointData.panel14Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk15.2.2.1

theorem panel14Prefix63_eq :
    P2RoundedFactorCheckpointData.panel14Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk15.2.2.2

end RHP2Bridge
