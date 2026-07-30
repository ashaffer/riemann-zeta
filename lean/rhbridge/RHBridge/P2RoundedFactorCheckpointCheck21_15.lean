import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk15 :
    P2RoundedFactorCheckpointData.panel21Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix60_eq :
    P2RoundedFactorCheckpointData.panel21Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk15.1

theorem panel21Prefix61_eq :
    P2RoundedFactorCheckpointData.panel21Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk15.2.1

theorem panel21Prefix62_eq :
    P2RoundedFactorCheckpointData.panel21Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk15.2.2.1

theorem panel21Prefix63_eq :
    P2RoundedFactorCheckpointData.panel21Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk15.2.2.2

end RHP2Bridge
