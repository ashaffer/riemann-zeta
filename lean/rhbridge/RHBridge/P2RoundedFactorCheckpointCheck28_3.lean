import RHBridge.P2RoundedFactorCheckpointData28

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FactorChunk3 :
    P2RoundedFactorCheckpointData.panel28Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨28, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel28Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨28, by decide⟩ := by
  decide +kernel

theorem panel28Prefix12_eq :
    P2RoundedFactorCheckpointData.panel28Prefix12 =
      normalizedPrefixTermAtomApprox ⟨12, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk3.1

theorem panel28Prefix13_eq :
    P2RoundedFactorCheckpointData.panel28Prefix13 =
      normalizedPrefixTermAtomApprox ⟨13, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk3.2.1

theorem panel28Prefix14_eq :
    P2RoundedFactorCheckpointData.panel28Prefix14 =
      normalizedPrefixTermAtomApprox ⟨14, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk3.2.2.1

theorem panel28Prefix15_eq :
    P2RoundedFactorCheckpointData.panel28Prefix15 =
      normalizedPrefixTermAtomApprox ⟨15, by decide⟩ ⟨28, by decide⟩ := by
  exact panel28FactorChunk3.2.2.2

end RHP2Bridge
