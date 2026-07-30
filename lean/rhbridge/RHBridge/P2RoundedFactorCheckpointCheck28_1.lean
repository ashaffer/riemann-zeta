import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk1 :
    P2RoundedFactorCheckpointData.panel28Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix4_eq :
    P2RoundedFactorCheckpointData.panel28Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk1.1

theorem panel28Prefix5_eq :
    P2RoundedFactorCheckpointData.panel28Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk1.2.1

theorem panel28Prefix6_eq :
    P2RoundedFactorCheckpointData.panel28Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk1.2.2.1

theorem panel28Prefix7_eq :
    P2RoundedFactorCheckpointData.panel28Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk1.2.2.2

end RHP2Bridge
